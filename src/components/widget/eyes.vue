<script setup lang="ts">
import type { Ref } from "#imports";
import { clamp, useMouse } from "@vueuse/core";

const { x: mouseX, y: mouseY } = useMouse();

/**
 * Make a reactive inline style that should be applied to a pupil inside the given eye element
 */
function makePupilStyle(eye: Ref<HTMLDivElement | null>): Ref<string> {
    return computed(() => {
        if (eye.value == null) {
            return "";
        }

        const eyeRect = eye.value!.getBoundingClientRect();
        const eyeMid = {
            x: eyeRect.left + eyeRect.width / 2,
            y: eyeRect.top + eyeRect.height / 2,
        };

        const relativeMouseX = mouseX.value - eyeMid.x;
        const relativeMouseY = mouseY.value - eyeMid.y;
        let angle = (Math.atan(relativeMouseY / relativeMouseX) * 180) / Math.PI;

        if (relativeMouseX > 0) {
            angle = 180 + angle;
        }

        return `transform: rotateZ(${angle}deg);`;
    });
}

const eye1 = ref(null);
const pupil1Style = makePupilStyle(eye1);
const eye2 = ref(null);
const pupil2Style = makePupilStyle(eye2);
</script>

<template>
    <div class="flex gap-0.5">
        <div class="eye" ref="eye1">
            <div class="pupil" :style="pupil1Style" />
        </div>
        <div class="eye" ref="eye2">
            <div class="pupil" :style="pupil2Style" />
        </div>
    </div>
</template>

<style scoped>
.eye {
    background-color: white;
    border-radius: 50%;
    height: 1rem;
    width: 1.25rem;
}

.eye > .pupil {
    position: relative;
    top: calc(0.5rem - (0.375rem / 2));
    left: 0.04rem;
    transform-origin: calc(1.25rem / 2 - 0.04rem) center;
    background-color: black;
    border-radius: 50%;
    height: 0.375rem;
    width: 0.375rem;
}
</style>
