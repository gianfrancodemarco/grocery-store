<template>
  <v-container fluid>
    <validation-observer ref="observer" v-slot="{ invalid }">
      <form @submit.prevent="onSubmit" @reset.prevent="onReset">
        <v-card class="ma-3 pa-3">
          <v-card-title primary-title>
            <div class="headline primary--text">Edit Sensor</div>
          </v-card-title>
          <v-card-text>
            <div class="my-3">
              <div class="subheading secondary--text text--lighten-2">Id</div>
              <div v-if="sensor" class="title primary--text text--darken-2">
                {{ sensor.id }}
              </div>
              <div v-else class="title primary--text text--darken-2">-----</div>
            </div>
            <validation-provider v-slot="{ errors }" name="Name" rules="required">
              <v-text-field
                v-model="sensor.name"
                label="Name"
                required
                :error-messages="errors"
              ></v-text-field>
            </validation-provider>
            <validation-provider v-slot="{ errors }" rules="required" name="Symptoms">
              <v-text-field
                v-model="sensor.symptoms"
                label="Symptoms"
                required
                :error-messages="errors"
              ></v-text-field>
            </validation-provider>
            <validation-provider v-slot="{ errors }" name="Fruits">
              <v-select
                class="mt-7"
                v-model="sensor.fruits"
                :items="fruits"
                multiple
                label="Fruits that can cause this sensor"
                :error-messages="errors"
                :item-text="(item) => `${item.id} - ${item.name}`"
                item-value="id"
                dense
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
import { ISensorUpdate } from "@/interfaces";
import { dispatchGetSensor, dispatchUpdateSensor } from "@/store/sensors/actions";
import { dispatchGetFruits } from "@/store/fruits/actions";
import { readFruits } from "@/store/fruits/getters";
import { readSensor } from "@/store/sensors/getters";
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
export default class EditSensor extends Vue {
  $refs!: {
    observer: InstanceType<typeof ValidationObserver>;
  };

  public async mounted() {
    await dispatchGetSensor(this.$store, { id: this.$route.params.id });
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

    const updatedSensor: ISensorUpdate = {
      id: this.sensor.id,
      name: this.sensor.name,
      symptoms: this.sensor.symptoms,
      fruits: this.sensor.fruits,
    };

    await dispatchUpdateSensor(this.$store, {
      id: this.sensor.id,
      sensor: updatedSensor,
    });

    this.$router.push("/main/sensors");
  }
  get sensor() {
    return readSensor(this.$store)
    // const sensorFromStore = readSensor(this.$store);
    // return {
    //   ...sensorFromStore,
    //   fruits: sensorFromStore?.fruits?.map((el) => el.id),
    // };
  }
  get fruits() {
    return readFruits(this.$store);
  }
}
</script>
