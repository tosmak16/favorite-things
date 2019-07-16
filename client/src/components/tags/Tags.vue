<template>
  <div>
    <section>
      <b-field v-if="tagList" grouped group-multiline>
        <div v-for="(item, index) in tagList" :key="index" class="control">
          <b-taglist attached>
            <b-tag class="tag-small" type="is-primary">{{
              item.dataKey
            }}</b-tag>
            <b-tag class="tag-small" type="is-dark">{{ item.type }}</b-tag>
            <b-tag
              name="index"
              @close="removeTag(index)"
              type="is-primary"
              :closable="closable"
              class="tag"
            >
              {{ item.type === "Date" ? moment(item.value) : item.value }}
            </b-tag>
          </b-taglist>
        </div>
      </b-field>
    </section>
  </div>
</template>

<style lang="scss" scoped>
@import "./Tags.scss";
</style>

<script>
import moment from "moment";

export default {
  name: "Tags",
  props: {
    tagList: Array,
    removeTag: Function,
    closable: Boolean
  },

  methods: {
    moment(date) {
      return moment(date).format("YYYY-MM-DD");
    }
  }
};
</script>
