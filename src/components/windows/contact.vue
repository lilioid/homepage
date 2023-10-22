<script setup lang="ts"></script>

<template>
    <div>
        <a class="contact-line" href="mailto:contact@finn-thorben.me">
            <SvgIcon path="{mdiEmail}" />
            <span>contact@finn-thorben.me</span>
        </a>

        <a class="contact-line" href="https://github.com/ftsell">
            <SvgIcon path="{mdiGithub}" />
            <span>ftsell</span>
        </a>

        <p>
            If you are using PGP and deem my website a valid method of identification, my public key is
            available for download from
            <a
                href="https://keys.openpgp.org/search?q=E28C78646FA4F70B30422385A78A03C25A3A3825"
                target="_blank"
                >keys.openpgp.org</a
            >
            or directly from <a rel="external" href="/finn-thorben_sell.gpg">here</a>.<br />
            Its fingerprint is:
        </p>

        <code>E28C78646FA4F70B30422385A78A03C25A3A3825</code>
    </div>
</template>
