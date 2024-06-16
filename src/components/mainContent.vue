<template>
    <v-card image="@/assets/castle-bg.jpg">
        <template v-slot:image>
            <v-img gradient="to top right, rgba(18,18,18,.8), rgba(18,18,18,.8)"></v-img>
        </template>
        <div class="d-flex">
            <appContent />
            <serverStatus />
            <RankingComponent />
        </div>

    </v-card>
</template>

<script>
import appContent from "@/components/appContent.vue";
import serverStatus from "@/components/serverStatus.vue"
import RankingComponent from "@/components/rankingComponent.vue";

</script>