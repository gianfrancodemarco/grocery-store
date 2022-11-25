<template>
  <v-container fluid>
    <validation-observer ref="observer" v-slot="{ invalid }">
      <form @submit.prevent="onSubmit" @reset.prevent="onReset">
        <v-card class="ma-3 pa-3">
          <v-card-title primary-title>
            <div class="headline primary--text">Create Analysis</div>
          </v-card-title>
          <v-card-text>
            <div class="my-3">
              <div class="subheading secondary--text text--lighten-2">Id</div>
              <div v-if="analysis" class="title primary--text text--darken-2">
                {{ "-" }}
              </div>
              <div v-else class="title primary--text text--darken-2">-----</div>
            </div>
            <validation-provider v-slot="{ errors }" rules="required" name="Sensor id">
              <v-select
                v-model="analysis.sensor_id"
                :items="sensors"
                label="Sensor"
                :error-messages="errors"
                :item-text="(item) => `${item.id} - ${item.name}, for ${item.fruit_size} fruits`"
                item-value="id"
                dense
              />
            </validation-provider>
            <validation-provider v-slot="{ errors }" rules="required" name="Lot id">
              <v-select
                v-model="analysis.lot_id"
                :items="lots"
                label="Lot id"
                :error-messages="errors"
                :item-text="(item) => `${item.id} - ${item.name} of ${item.fruit.size} fruits`"
                item-value="id"
                dense
              />
            </validation-provider>
            <validation-provider
              v-slot="{ errors }"
              rules="required"
              name="Description"
            >
              <v-text-field
                v-model="analysis.description"
                label="Description"
                required
                :error-messages="errors"
              ></v-text-field>
            </validation-provider>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn @click="cancel">Cancel</v-btn>
            <v-btn :disabled="invalid" type="submit" color="primary"> Save </v-btn>
          </v-card-actions>
        </v-card>
      </form>
    </validation-observer>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import { IAnalysisCreate } from "@/interfaces";
import { dispatchCreateAnalysis } from "@/store/analysiss/actions";
import { dispatchGetLots } from "@/store/lots/actions";
import { dispatchGetSensors } from "@/store/sensors/actions";
import { readLots } from "@/store/lots/getters";
import { readSensors } from "@/store/sensors/getters";
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
export default class EditAnalysis extends Vue {
  $refs!: {
    observer: InstanceType<typeof ValidationObserver>;
  };

  public analysis: IAnalysisCreate = {
    id: null,
    fruit_id: null,
    lot_id: null,
    description: null
  };

  public async mounted() {
    await dispatchGetLots(this.$store);
    await dispatchGetSensors(this.$store);
  }

  public cancel() {
    this.$router.back();
  }

  public async onSubmit() {
    const success = await this.$refs.observer.validate();
    if (!success) {
      return;
    }

    const updatedAnalysis: IAnalysisCreate = {
      lot_id: this.analysis.lot_id,
      sensor_id: this.analysis.sensor_id,
      description: this.analysis.description,
    };

    await dispatchCreateAnalysis(this.$store, {
      analysis: updatedAnalysis,
    });

    this.$router.push("/main/analysiss");
  }
  get lots() {
    return readLots(this.$store);
  }
  get sensors() {
    return readSensors(this.$store);
  }
}
</script>
