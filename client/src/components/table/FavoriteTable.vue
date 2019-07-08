<template>
  <section>
    <b-table
      striped
      hoverable
      :data="favoriteList.results"
      :loading="loading"
      paginated
      backend-pagination
      :total="favoriteList.count"
      :per-page="perPage"
      @page-change="onPageChange"
      aria-next-label="Next page"
      aria-previous-label="Previous page"
      aria-page-label="Page"
      aria-current-label="Current page"
      backend-sorting
      :default-sort-direction="defaultSortOrder"
      :default-sort="[sortField, sortOrder]"
      @sort="onSort"
      v-if="categoryList.length"
      @click="onClick"
      focusable
      isEmpty
      class="table"
    >
      <template slot-scope="props">
        <b-table-column field="original_title" label="Title">
          {{ props.row.title }}
        </b-table-column>

        <b-table-column field="ranking" label="Ranking" centered sortable>
          <span>
            {{ props.row.ranking }}
          </span>
        </b-table-column>

        <b-table-column field="category" label="Category" centered sortable>
          {{ getCategoryName(props.row.category) }}
        </b-table-column>

        <b-table-column
          field="created_date"
          label="Added time"
          sortable
          centered
        >
          {{ new Date(props.row.created_date) | moment }}
        </b-table-column>

        <b-table-column
          field="modified_date"
          label="Updated time"
          sortable
          centered
        >
          {{ new Date(props.row.modified_date) | moment }}
        </b-table-column>

        <b-table-column class="description" label="Description">
          {{ props.row.description || "......" }}
        </b-table-column>

        <b-table-column width="300" field="metadata" label="Tags">
          <Tags :tag-list="props.row.metadata" :remove-tag="() => {}" />
        </b-table-column>
      </template>

      <template slot="empty">
        <section class="section">
          <div class="content has-text-grey has-text-centered">
            <p>
              <b-icon icon="emoticon-sad" size="is-large"> </b-icon>
            </p>
            <p>
              Nothing here. Click the icon below to add your favorite things
            </p>
          </div>
        </section>
      </template>
    </b-table>
  </section>
</template>

<style lang="scss" scoped>
td {
  text-transform: capitalize;
  height: 100px;

  @media (max-width: 500px) {
    min-height: 80px;
    height: 100%;
  }
}

.table {
  box-shadow: 0px 1px 12px #c1bfbf;
  padding: 10px;
}

.description {
  width: min-content;
}
</style>

<script>
import { mapGetters } from "vuex";
import moment from "moment";

import Tags from "../tags/Tags";

export default {
  name: "FavoriteTable",
  components: { Tags },
  props: {
    onClick: Function
  },
  data() {
    return {
      loading: false,
      sortField: "modified_date",
      sortOrder: "desc",
      defaultSortOrder: "desc",
      page: 1,
      perPage: 5
    };
  },

  computed: {
    ...mapGetters(["favoriteList", "categoryList", "selectedCategory"])
  },

  watch: {},
  methods: {
    loadAsyncData(page = 1, ordering = "-modified_date") {
      const token = localStorage.getItem("token");
      this.$store.dispatch("getFavorites", {
        token,
        page,
        ordering,
        category: this.selectedCategory
      });
    },
    onPageChange(page) {
      this.page = page;
      const orderingField =
        this.sortOrder === "desc" ? `-${this.sortField}` : this.sortField;

      this.loadAsyncData(page, orderingField);
    },
    /*
     * Handle sort event
     */
    onSort(field, order) {
      this.sortField = field;
      this.sortOrder = order;
      const orderingField = order === "desc" ? `-${field}` : field;
      this.loadAsyncData(this.page, orderingField);
    },

    getCategoryName(categoryId) {
      if (!categoryId || !this.categoryList) return "";
      const { name } = this.categoryList.find(item => item.id === categoryId);
      return name;
    }
  },
  mounted() {
    this.loadAsyncData();
  },
  filters: {
    moment(date) {
      return moment(date).fromNow();
    }
  }
};
</script>
