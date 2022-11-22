<template>
  <v-container fluid>
    <validation-observer ref="observer" v-slot="{ invalid }">
      <form @submit.prevent="onSubmit" @reset.prevent="onReset">
        <v-card class="ma-3 pa-3">
          <v-card-title primary-title>
            <div class="headline primary--text">Create Sensor</div>
          </v-card-title>
          <v-card-text>
            <div class="my-3">
              <div class="subheading secondary--text text--lighten-2">Id</div>
              <div v-if="sensor" class="title primary--text text--darken-2">
                {{ "-" }}
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
            <validation-provider v-slot="{ errors }" name="medium_energy_consumption" rules="required">
              <v-text-field
                v-model="sensor.medium_energy_consumption"
                label="Medium Energy Consumption"
                required
                :error-messages="errors"
                type="number"
              ></v-text-field>
            </validation-provider>
            <validation-provider v-slot="{ errors }" name="cost" rules="required">
              <v-text-field
                v-model="sensor.cost"
                label="Cost"
                required
                :error-messages="errors"
                type="number"
              ></v-text-field>
            </validation-provider>
            <validation-provider v-slot="{ errors }" name="Brand" rules="required">
              <v-text-field
                v-model="sensor.brand"
                label="Brand"
                required
                :error-messages="errors"
              ></v-text-field>
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
import { ISensorCreate } from "@/interfaces";
import { dispatchCreateSensor } from "@/store/sensors/actions";
import { dispatchGetFruits } from "@/store/fruits/actions";
import { readFruits } from "@/store/fruits/getters";
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

  public sensor: ISensorCreate = {
    name: null,
    fruit_size: "MEDIUM",
    medium_energy_consumption: 1,
    cost: 50,
    brand: null
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

    const updatedSensor: ISensorCreate = {
      name: this.sensor.name,
      symptoms: this.sensor.symptoms,
      fruits: this.sensor.fruits,
    };

    await dispatchCreateSensor(this.$store, {
      sensor: updatedSensor,
    });

    this.$router.push("/main/sensors");
  }
  get fruits() {
    return readFruits(this.$store);
  }
}
</script>
