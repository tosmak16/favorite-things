<template>
  <div class="table-bg ">
    <h2>
      Audit Logs
    </h2>
    <section>
      <b-table
        :data="auditLogList.results"
        :loading="loading"
        paginated
        backend-pagination
        :total="auditLogList.count"
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
        v-if="auditLogList"
      >
        <template slot-scope="props">
          <b-table-column field="activity" label="Activity">
            {{ props.row.activity }}
          </b-table-column>

          <b-table-column
            class="tag-wrapper"
            field="action"
            label="Action"
            centered
          >
            <b-taglist v-if="props.row.action === `created`" attached>
              <b-tag type="is-dark">{{ props.row.action }}</b-tag>
              <b-tag type="is-success"></b-tag>
            </b-taglist>
            <b-taglist v-if="props.row.action === `updated`" attached>
              <b-tag type="is-dark">{{ props.row.action }}</b-tag>
              <b-tag type="is-info"></b-tag>
            </b-taglist>
            <b-taglist v-if="props.row.action === `deleted`" attached>
              <b-tag type="is-dark">{{ props.row.action }}</b-tag>
              <b-tag type="is-danger"></b-tag>
            </b-taglist>
          </b-table-column>

          <b-table-column
            field="created_date"
            label="Added time"
            sortable
            centered
          >
            {{ new Date(props.row.created_date) | moment }}
          </b-table-column>
        </template>
      </b-table>
    </section>
  </div>
</template>

<style lang="scss" scoped>
td {
  text-transform: capitalize;
  height: 80px;
  width: 300px;

  @media (max-width: 500px) {
    min-height: 80px;
    height: 100%;
  }
}

.table-bg {
  z-index: 1000 !important;
  background-color: white;
  padding: 10px;
}

.tag-wrapper {
  display: flex;
  justify-content: center;
}
</style>

<script>
import { mapGetters } from "vuex";
import moment from "moment";

export default {
  name: "AuditLogTable",
  data() {
    return {
      loading: false,
      sortField: "created_date",
      sortOrder: "desc",
      defaultSortOrder: "desc",
      page: 1,
      perPage: 5
    };
  },

  computed: {
    ...mapGetters(["auditLogList"])
  },

  watch: {},
  methods: {
    loadAsyncData(page = 1, ordering = "-created_date") {
      const token = localStorage.getItem("token");
      this.$store.dispatch("getAuditLogs", { token, page, ordering });
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
