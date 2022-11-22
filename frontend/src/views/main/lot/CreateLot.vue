<template>
  <v-container fluid>
    <validation-observer ref="observer" v-slot="{ invalid }">
      <form @submit.prevent="onSubmit" @reset.prevent="onReset">
        <v-card class="ma-3 pa-3">
          <v-card-title primary-title>
            <div class="headline primary--text">Create Lot</div>
          </v-card-title>
          <v-card-text>
            <div class="my-3">
              <div class="subheading secondary--text text--lighten-2">Id</div>
              <div v-if="lot" class="title primary--text text--darken-2">
                {{ "-" }}
              </div>
              <div v-else class="title primary--text text--darken-2">-----</div>
            </div>
            <validation-provider v-slot="{ errors }" name="Name" rules="required">
              <v-text-field
                v-model="lot.name"
                label="Name"
                required
                :error-messages="errors"
              ></v-text-field>
            </validation-provider>
            <validation-provider v-slot="{ errors }" rules="required" name="Fruit id">
              <v-select
                v-model="lot.fruit_id"
                :items="fruits"
                label="Fruit id"
                :error-messages="errors"
                :item-text="(item) => `${item.id} - ${item.name}`"
                item-value="id"
                dense
              />
            </validation-provider>
            <validation-provider v-slot="{ errors }" rules="required" name="Arrival">
              <v-text-field
                label="Arrival"
                :value="computedDateFormatted"
                @input="value => lot.timestamp_arrival = value"
                type="datetime-local"
                :error-messages="errors"
              />
            </validation-provider>
            <validation-provider v-slot="{ errors }" rules="required" name="Volume">
              <v-text-field
                v-model="lot.volume"
                label="Volume (m^3)"
                required
                :error-messages="errors"
                type="number"
                min="0"
              />
            </validation-provider>
            <validation-provider v-slot="{ errors }" rules="required" name="Weight">
              <v-text-field
                v-model="lot.weight"
                label="Weight (kg)"
                required
                :error-messages="errors"
                type="number"
                min="0"
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
import { ILotCreate } from "@/interfaces";
import { dispatchCreateLot } from "@/store/lots/actions";
import { dispatchGetFruits } from "@/store/fruits/actions";
import { readFruits } from "@/store/fruits/getters";
import { ValidationProvider, ValidationObserver, extend } from "vee-validate";
import { required, confirmed, email } from "vee-validate/dist/rules";
import { format } from "date-fns";

extend("required", { ...required, message: "{_field_} can not be empty" });
extend("confirmed", { ...confirmed, message: "Passwords do not match" });
extend("email", { ...email, message: "Invalid email address" });

@Component({
  components: {
    ValidationObserver,
    ValidationProvider,
  },
})
export default class EditLot extends Vue {
  $refs!: {
    observer: InstanceType<typeof ValidationObserver>;
  };

  public lot: ILotCreate = {
    name: null,
    fruit_id: null,
    timestamp_arrival: new Date(),
    volume: 1,
    weight: 1
  };

  public async mounted() {
    await dispatchGetFruits(this.$store);
  }

  public cancel() {
    this.$router.back();
  }

  public async onSubmit() {
    const success = await this.$refs.observer.validate();
    if (!success) {
      return;
    }

    const updatedLot: ILotCreate = {
      name: this.lot.name,
      fruit_id: this.lot.fruit_id,
      timestamp_arrival: format(new Date(this.lot.timestamp_arrival), "yyyy-MM-dd'T'HH:mm:ss"),
      volume: this.lot.volume,
      weight: this.lot.weight
    };

    await dispatchCreateLot(this.$store, {
      id: this.lot.id,
      lot: updatedLot,
    });

    this.$router.push("/main/lots");
  }
  get fruits() {
    return readFruits(this.$store);
  }
  get computedDateFormatted(){
    return this.lot.timestamp_arrival ? format(new Date(this.lot.timestamp_arrival), "yyyy-MM-dd'T'HH:mm") : null;
  }
}
</script>
