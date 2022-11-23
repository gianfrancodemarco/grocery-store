<template>
  <v-container fluid>
    <validation-observer ref="observer" v-slot="{ invalid }">
      <form @submit.prevent="onSubmit" @reset.prevent="onReset">
        <v-card class="ma-3 pa-3">
          <v-card-title primary-title>
            <div class="headline primary--text">Edit Fruit</div>
          </v-card-title>
          <v-card-text>
            <div class="my-3">
              <div class="subheading secondary--text text--lighten-2">Id</div>
              <div v-if="fruit" class="title primary--text text--darken-2">
                {{ fruit.id }}
              </div>
              <div v-else class="title primary--text text--darken-2">-----</div>
            </div>
            <validation-provider v-slot="{ errors }" name="Name" rules="required">
              <v-text-field
                v-model="fruit.name"
                label="Name"
                required
                :error-messages="errors"
              ></v-text-field>
            </validation-provider>
            <validation-provider v-slot="{ errors }" name="Size" rules="required">
             <v-select
                class="mt-7"
                v-model="fruit.size"
                :items="['LITTLE', 'MEDIUM', 'BIG']"
                label="Size"
                :error-messages="errors"
                dense
              />
            </validation-provider>
            <validation-provider v-slot="{ errors }" rules="required" name="Peel type">
              <v-select
                class="mt-7"
                v-model="fruit.peel_type"
                :items="['NOT EDIBLE', 'EDIBLE']"
                label="Peel Type"
                :error-messages="errors"
                dense
              ></v-select>
            </validation-provider>
            <validation-provider
              v-slot="{ errors }"
              name="Maximum stationary time"
              rules="required"
            >
              <v-text-field
                v-model="fruit.maximum_stationary_time"
                label="Maximum stationary time"
                required
                :default="24"
                :error-messages="errors"
                :min="0"
                type="number"
                step="0.01"
              ></v-text-field>
            </validation-provider>
            <validation-provider v-slot="{ errors }" rules="required" name="Base price">
              <v-text-field
                v-model="fruit.base_price"
                label="Base price"
                required
                :error-messages="errors"
                type="number"
                step="0.01"
                min="0"               
                hint="A price multiplier"
                persistent-hint
              />
            </validation-provider>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn @click="cancel">Cancel</v-btn>
            <v-btn :disabled="invalid" type="submit"> Save </v-btn>
          </v-card-actions>
        </v-card>
      </form>
    </validation-observer>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import { IFruitUpdate } from "@/interfaces";
import { dispatchGetFruit, dispatchUpdateFruit } from "@/store/fruits/actions";
import { readFruit } from "@/store/fruits/getters";
import { ValidationProvider, ValidationObserver, extend } from "vee-validate";
import { required, confirmed, email } from "vee-validate/dist/rules";

extend("required", { ...required, message: "{_field_} can not be empty" });
extend("confirmed", { ...confirmed, message: "Passwords do not match" });
extend("email", { ...email, message: "Invalid email address" });

@Component({
  components: {
    ValidationObserver,
    ValidationProvider,
  },
})
export default class EditFruit extends Vue {
  $refs!: {
    observer: InstanceType<typeof ValidationObserver>;
  };

  public async mounted() {
    await dispatchGetFruit(this.$store, { id: this.$route.params.id });
  }

  public cancel() {
    this.$router.back();
  }

  public async onSubmit() {
    const success = await this.$refs.observer.validate();
    if (!success) {
      return;
    }

    const updatedFruit: IFruitUpdate = {
      id: this.fruit.id,
      name: this.fruit.name,
      size: this.fruit.size,
      peel_type: this.fruit.peel_type,
      maximum_stationary_time: this.fruit.maximum_stationary_time,
      base_price: this.fruit.base_price
    };

    await dispatchUpdateFruit(this.$store, {
      id: this.fruit.id,
      fruit: updatedFruit,
    });

    this.$router.push("/main/fruits");
  }
  get fruit() {
    return readFruit(this.$store);
  }
}
</script>
