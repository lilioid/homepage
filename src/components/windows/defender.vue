<script setup lang="ts">
import rickRoll from "~/assets/rick_roll.webm";
</script>

<template>
    <div>
        <video :src="rickRoll" loop autoplay class="h-[600px]"></video>
        <p>
            <span>Source:</span>
            <a href="https://youtu.be/dQw4w9WgXcQ">YouTube: Rick Astley - Never Gonna Give You Up</a>
        </p>
    </div>
</template>
