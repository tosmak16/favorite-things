<template>
  <div class="form-group">
    <div class="control">
      <label for="dataKey">Key</label>
      <input
        v-model="dataKey"
        id="dataKey"
        name="key"
        class="input"
        type="text"
        v-validate="'required'"
        placeholder="Enter dataKey"
      />
      <span class="error-label">{{ errors.first("key") }}</span>
    </div>

    <div class="control">
      <label for="categroy">Type</label>
      <b-select
        name="categroy"
        id="categroy"
        expanded
        placeholder="Select category"
        v-model="type"
      >
        <option v-for="type in metaDataType" :value="type" :key="type">
          {{ type }}
        </option>
      </b-select>
    </div>

    <div v-if="type === `Text`" class="control">
      <label for="Text">Value</label>
      <input
        v-model="value"
        id="Text"
        name="value"
        class="input"
        type="text"
        v-validate="'required'"
        placeholder="Enter value"
      />
      <span class="error-label">{{ errors.first("value") }}</span>
    </div>

    <div v-if="type === `Number`" class="control">
      <label for="value">Value</label>
      <input
        v-model="value"
        id="value"
        name="value"
        class="input"
        type="Number"
        v-validate="'required'"
        placeholder="Enter value"
        min="0"
      />
      <span class="error-label">{{ errors.first("value") }}</span>
    </div>

    <div v-if="type === `Date`" class="control">
      <label for="value">Value</label>
      <b-datepicker
        placeholder="Type or select a date..."
        icon="calendar-today"
        editable
        v-model="date"
        name="value"
      >
      </b-datepicker>
      <span class="error-label">{{ errors.first("value") }}</span>
    </div>

    <button @click="onClick" class="button is-success is-outlined">
      Add
    </button>
  </div>
</template>

<style lang="scss" scoped>
@import "./MetaData.scss";
.error-label {
  color: orangered;
}
</style>

<script>
export default {
  name: "MetaData",
  props: {
    onAddMeta: Function
  },
  data: () => ({
    dataKey: "",
    type: "Text",
    value: "",
    date: new Date(),
    metaDataType: ["Text", "Number", "Date"]
  }),
  methods: {
    async onClick() {
      const isValid = await this.$validator.validate();
      if (isValid === false) return;

      this.onAddMeta({
        dataKey: this.dataKey,
        type: this.type,
        value: this.type === "Date" ? this.date : this.value
      });
    }
  }
};
</script>
