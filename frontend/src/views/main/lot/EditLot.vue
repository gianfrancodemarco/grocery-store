<template>
  <v-container fluid>
    <validation-observer ref="observer" v-slot="{ invalid }">
      <form @submit.prevent="onSubmit" @reset.prevent="onReset">
        <v-card class="ma-3 pa-3">
          <v-card-title primary-title>
            <div class="headline primary--text">Edit Lot </div>
            <v-spacer/>
            <div class="headline primary--text mr-4">{{lot.on_display ? "On Display" : "Not on display"}}</div>
            <v-btn 
              color="primary" 
              @click="toggleLotOnDisplay"
            > 
            {{lot.on_display ? "Remove from display" : "Put on display"}} 
            </v-btn>
          </v-card-title>
          <v-card-text>
            <div class="my-3">
              <div class="subheading secondary--text text--lighten-2">Id</div>
              <div v-if="lot" class="title primary--text text--darken-2">
                {{ lot.id }}
              </div>
              <div v-else class="title primary--text text--darken-2">-----</div>
            </div>
            <validation-provider v-slot="{ errors }" name="Name" rules="required">
              <v-text-field
                v-model="lot.name"
                label="Name"
                required
                :error-messages="errors"
              />
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
                step="0.01"
              />
            </validation-provider>
            <validation-provider v-slot="{ errors }" rules="required" name="Weight">
              <v-text-field
                v-model="lot.weight"
                label="Weight (kg)"
                required
                :error-messages="errors"
                type="number"
                step="0.01"
                min="0"
              />
            </validation-provider>
            <validation-provider v-slot="{ errors }" rules="required" name="Ripens level">
              <v-text-field
                v-model="lot.ripens_level"
                label="Ripens level"
                required
                :error-messages="errors"
                type="number"
                step="0.01"
                min="0"
                max="1"
                hint="Goes from 0 (unripe) to 1 (rotten)"
                persistent-hint
              />
            </validation-provider>
            <validation-provider v-slot="{ errors }" rules="required" name="Price">
              <v-text-field
                v-model="lot.price"
                label="Price"
                required
                :error-messages="errors"
                type="number"
                disabled
                hint="The price will be calculated automatically"
                persistent-hint
              />
            </validation-provider>
            <validation-provider v-slot="{ errors }" rules="required" name="Expired">
              <v-text-field
                class="mt-6"
                v-model="lot.expired"
                label="Expired"
                :error-messages="errors"
                disabled
                dense
              />
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
import { ILotUpdate } from "@/interfaces";
import { dispatchGetLot, dispatchUpdateLot } from "@/store/lots/actions";
import { readLot } from "@/store/lots/getters";
import { dispatchGetFruits } from "@/store/fruits/actions";
import { readFruits } from "@/store/fruits/getters";
import { ValidationProvider, ValidationObserver, extend } from "vee-validate";
import { required } from "vee-validate/dist/rules";
import { format } from "date-fns";

extend("required", { ...required, message: "{_field_} can not be empty" });

@Component({
  components: {
    ValidationObserver,
    ValidationProvider
  },
})
export default class EditLot extends Vue {
  $refs!: {
    observer: InstanceType<typeof ValidationObserver>;
  };
  menu1: false;

  public async mounted() {
    await dispatchGetLot(this.$store, { id: this.$route.params.id });
    await dispatchGetFruits(this.$store);
  }
  public cancel() {
    this.$router.back();
  }
  
  public async toggleLotOnDisplay(){
    
    const updatedLot: ILotUpdate = {
      id: this.lot.id,
      on_display: !this.lot.on_display
    };

    await dispatchUpdateLot(this.$store, {
      id: this.lot.id,
      lot: updatedLot,
    });

    await dispatchGetLot(this.$store, { id: this.$route.params.id });

  }
  
  public async onSubmit() {
    const success = await this.$refs.observer.validate();
    if (!success) {
      return;
    }

    const updatedLot: ILotUpdate = {
      id: this.lot.id,
      name: this.lot.name,
      fruit_id: this.lot.fruit_id,
      timestamp_arrival: format(new Date(this.lot.timestamp_arrival), "yyyy-MM-dd'T'HH:mm:ss"),
      volume: this.lot.volume,
      weight: this.lot.weight,
      ripens_level: this.lot.ripens_level
    };

    await dispatchUpdateLot(this.$store, {
      id: this.lot.id,
      lot: updatedLot,
    });

    this.$router.push("/main/lots");
  }
  get lot() {
    return readLot(this.$store);
  }
  get fruits() {
    return readFruits(this.$store);
  }
  get computedDateFormatted(){
    return this.lot.timestamp_arrival ? format(new Date(this.lot.timestamp_arrival), "yyyy-MM-dd'T'HH:mm") : null;
  }
}
</script>
