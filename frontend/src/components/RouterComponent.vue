<template>
  <router-view :key="$route.fullPath"></router-view>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";

@Component
export default class RouterComponent extends Vue {}
</script>
