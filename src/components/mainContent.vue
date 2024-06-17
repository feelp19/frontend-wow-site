<template>
    <v-card image="@/assets/castle-bg.jpg">
        <template v-slot:image>
            <v-img gradient="to top right, rgba(18,18,18,.8), rgba(18,18,18,.8)"></v-img>
        </template>
        <div class="d-flex flex-wrap">
            <appContent />
            <serverStatus />
            <rankingComponent />
        </div>
    </v-card>
</template>

<script>
import appContent from "@/components/appContent.vue";
import serverStatus from "@/components/serverStatus.vue"
import rankingComponent from "@/components/rankingComponent.vue";
</script>