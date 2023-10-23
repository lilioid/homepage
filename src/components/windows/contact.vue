<script setup lang="ts">
import { mdiEmail, mdiGithub } from "@mdi/js";
</script>

<template>
    <div class="m-2">
        <p class="mb-4">I'm active on many communication platforms, some of them are listed here:</p>

        <ul>
            <li>
                <a
                    class="flex gap-2 mb-4 underline decoration-link_blue text-link_blue"
                    href="mailto:contact@finn-thorben.me"
                >
                    <SvgIcon :path="mdiEmail" />
                    <span class="sr-only">E-Mail:</span>
                    <span>hi@ftsell.de</span>
                </a>
            </li>

            <li>
                <a
                    class="flex gap-2 mb-3 underline decoration-link_blue text-link_blue"
                    href="https://matrix.to/#/@17sell:mafiasi.de"
                    target="_blank"
                >
                    <img width="24" src="~/assets/matrix_icon.svg" alt="Matrix Icon" />
                    <span class="sr-only">Matrix:</span>
                    <span>@17sell:mafiasi.de</span>
                </a>
            </li>

            <li>
                <a
                    class="flex gap-2 underline decoration-link_blue text-link_blue"
                    href="https://github.com/ftsell"
                    target="_blank"
                >
                    <SvgIcon :path="mdiGithub" />
                    <span class="sr-only">GitHub:</span>
                    <span>ftsell</span>
                </a>
            </li>
        </ul>
    </div>
</template>
