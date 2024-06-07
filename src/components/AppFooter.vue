<template>
  <v-footer height="40" app>
    <a
      v-for="item in items"
      :key="item.title"
      :href="item.href"
      :title="item.title"
      class="d-inline-block mx-2 social-link social"
      rel="noopener noreferrer"
      target="_blank"
      style="text-decoration: none; font-size: 0.9rem"
    >
  {{ item.autor }}
      <v-icon
        :icon="item.icon"
        :size="item.icon === '$vuetify' ? 24 : 16"
      />
    </a>

    <div
      class="text-caption text-disabled"
      style="position: absolute; right: 16px;"
    >
      &copy{{ (new Date()).getFullYear() }} 
    </div>
  </v-footer>
</template>

<script setup>
  const items = [
    {
      title: 'feelp19 GitHub',
      icon: `mdi-github`,
      href: 'https://github.com/feelp19/',
      autor: 'Felipe de Pietro'
    },
    {
      title: 'Miguel Github',
      icon: 'mdi-github',
      href: 'https://github.com/MiguelKauadePietro/',
      autor: 'Miguel de Pietro'
    }
  ]
</script>

<style scoped lang="sass">
  .social-link :deep(.v-icon)
    color: rgba(var(--v-theme-on-background), var(--v-disabled-opacity))
    text-decoration: none
    transition: .2s ease-in-out

    &:hover
      color: rgba(25, 118, 210, 1)
</style>
