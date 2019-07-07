<template>
  <md-speed-dial :class="bottomPosition">
    <md-speed-dial-target>
      <md-icon>add</md-icon>
    </md-speed-dial-target>

    <md-speed-dial-content>
      <md-button @click="onShowAuditLogsIconClick" class="md-icon-button">
        <md-icon>folder</md-icon>
      </md-button>
      <md-button @click="onAddCategoryIconClick" class="md-icon-button">
        <md-icon>category</md-icon>
      </md-button>

      <md-button @click="onAddFavoriteIconClick" class="md-icon-button">
        <md-icon>note_add</md-icon>
      </md-button>
    </md-speed-dial-content>
  </md-speed-dial>
</template>

<style lang="scss" scoped>
@import "./SpeedDial.scss";
</style>

<script>
import Vue from "vue";

import { MdButton, MdSpeedDial, MdIcon } from "vue-material/dist/components";

import "vue-material/dist/vue-material.min.css";

Vue.use(MdButton);
Vue.use(MdSpeedDial);
Vue.use(MdIcon);

export default {
  name: "SpeedDial",
  props: {
    onAddFavoriteIconClick: Function,
    onAddCategoryIconClick: Function,
    onShowAuditLogsIconClick: Function
  },
  data: () => ({
    bottomPosition: "md-bottom-left"
  })
};
</script>
