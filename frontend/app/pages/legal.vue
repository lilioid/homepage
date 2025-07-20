<script setup lang="ts">
definePageMeta({
  name: "legal",
});
</script>

<template>
  <HCommand cmd="cat /legal/imprint.html">
    <section id="imprint">
      <h2 class="text-2xl font-extrabold mt-2 mb-4"><i>Not</i> Imprint</h2>
      <p>
        This is my private, non-commercial website therefore an imprint containing my private address and phone number
        is not necessary.<br>
        If you want to contact me you can choose your preferred network or method from the ones listed on the
        <NuxtLink :to="{ name: 'home' }">index page</NuxtLink>
        .
      </p>
    </section>
  </HCommand>

  <HCommand cmd="cat /legal/privacy-policy.html">
    <section id="privacy-policy">
      <h2 class="text-2xl font-extrabold mt-2 mb-4">Privacy Policy</h2>

      <h3 class="text-xl font-bold mb-3">Summary</h3>
      <p class="mb-8">
        In short, neither this website nor any programs associated with it perform any sort of tracking.
        Metadata is also only stored for a very small amount of time and never sold nor automatically analyzed.
      </p>

      <h3 class="text-xl font-bold mb-3 mt-8">Scope of Application</h3>
      <p class="mb-2">
        This policy applies to pages that explicitly link to it and are hosted on one of the following domains or any of
        their subdomains:
      </p>
      <ol class="mb-4 list-decimal list-inside pl-8">
        <li>lly.sh</li>
        <li>ftsell.de</li>
        <li>finn-thorben.me</li>
      </ol>

      <p class="mb-2">
        Additionally it applies to emails sent to and received from any addresses ending with the following domains:
      </p>
      <ol class="mb-4 list-decimal list-inside pl-8">
        <li>@lly.sh</li>
        <li>@ftsell.de</li>
        <li>@finn-thorben.me</li>
        <li>@timonengelke.de</li>
        <li>@bit-bots.de</li>
        <li>@sheaksadi.me</li>
        <li>@bastianpermesang.com</li>
        <li>@powolygon.gay</li>
      </ol>

      <h3 class="text-xl font-bold mb-3 mt-8">Collected Information</h3>
      <h4 class="text-xl">Web Services</h4>
      <p class="my-2">
        The webserver temporarily stores access and error logs which include details about a users request such as the
        client IP-Addresse, and which webpage was requested.
        The logs are purged regularly and never stored for longer than 48 hours.
      </p>
      <p class="my-2">
        The detailed nginx log format configuration can be seen below.
        Refer to the <a rel="external" href="http://nginx.org/en/docs/http/ngx_http_log_module.html">NGINX
        Documentation</a> for details about it.
      </p>

      <code class="block px-4 my-2">
        {"time": "$time_iso8601", "host": "$host", "status": "$status", "remote_addr": "$remote_addr", "request":
        "$request", "proxy_upstream": "$proxy_upstream_name", "request_length": "$request_length", "request_time":
        "$request_time" }
      </code>

      <h4 class="text-xl mt-4 mb-2">E-Mails</h4>
      <p>
        The mail server handling mails for the above mentioned domains which generates connection log entries when it
        receives E-Mails or sends E-Mails.
        The log contains information about the IP-Addresses and hostnames (determines via reverse-dns as well as
        SMTP-HELO) of connected clients as well as metadata about transferred mails.
        This metadata is limited to Recipient and Sender address of the mail, the content of the SMTP <code>RCPT
        TO</code> command and a unique ID per mail.
      </p>

      <h3 class="text-xl font-bold mb-3 mt-8">Purpose of Collection</h3>
      <p>
        The information collected is used to troubleshoot server errors and create IP or domain blocks when deemed
        necessary.
        The data is only stored on this server and will never be shared with any third party.
      </p>

    </section>
  </HCommand>
</template>
