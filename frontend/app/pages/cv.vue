<script setup lang="ts">
definePageMeta({
  name: "cv",
  path: "/cv.html",
});

useSeoMeta({
  title: "CV",
})
</script>

<template>
  <HCommand cmd="cat /cv.html">
    <section id="introduction">
      <h2 class="text-2xl font-extrabold mt-2 mb-4">Introduction</h2>
      <p>
        Hello there I'm Lilly Sell.<br/>
        I'm currently working at <a href="https://www.b1-systems.de/" rel="external">B1 Systems GmbH</a> and am not looking for employment.
        Regardless, I keep a list of my skills on this page if someone wants to know what I'm interested in or has a cool project idea.
      </p>
      <p>
        If you want to get in contact, please use one of the methods listed on my <NuxtLink :href="{ name: 'home' }">main page</NuxtLink>.
      </p>
    </section>

    <section id="skills">
      <h2 class="text-2xl font-extrabold mt-12 mb-4">Skills</h2>
      <p>
        My main area of expertise is linux system administration.
        I have experience maintaining a number of servers in different contexts ranging from personal server
        infrastructure and student IT services to business critical applications at my previous employers.
        For this purpose I prefer to use declarative toolings such as <i>Ansible</i>, <i>NixOs</i>, <i>Terraform</i>
        or <i>Kubernetes</i>.<br>
        The systems I maintained are also monitored by either <i>Prometheus + AlertManager</i> or <i>Icinga2</i>
        including
        automated alerting.
        I was also the person responsible for remediating issues based on alerts or colleague notifications.
      </p>
      <p>
        Apart from server administration, I am experienced in managing and maintaining network configurations for access
        networks as well as virtualized environments.
        This includes providing IP connectivity for workstations via DHCP, managing DNS resolvers and configuring
        routers as well as
        security considerations such as access separation via VLANs and other software defined networking technologies.
      </p>
      <p>
        I am also versed in software development and maintenance with most of my experience being in web application
        development and data processing with python.
        In this area I have contributed to different open source projects and developed many internal applications
        ranging from small tools to complex applications.
      </p>
      <div class="my-8 mx-16 grid grid-cols-[1fr_auto] lg:grid-cols-[1fr_auto_1fr_auto] gap-6 items-center">
        <HCVSkill name="Linux Server Administration" :level="10" />
        <HCVSkill name="Access Network Administration" :level="10" />
        <HCVSkill name="Virtualization Technologies (QEMU, libvirt, SDN, ...)" :level="7" />
        <HCVSkill name="OCI Container Technologies (e.g. Docker, Kubernetes)" :level="9" />
        <HCVSkill name="CI/CD Practices (Jenkins, GitHub Actions, Woodpecker, ArgoCD, ...)" :level="10" />
        <HCVSkill name="Python" :level="10" />
        <HCVSkill name="Rust" :level="9" />
        <HCVSkill name="Traditional Web Programing (HTML, CSS, Vanilla JS)" :level="8" />
        <HCVSkill name="Reactive Web Programming (Vue, Svelte, ...)" :level="7" />
      </div>
    </section>

    <section id="cv">
      <h2 class="text-2xl font-extrabold mt-12 mb-4">CV</h2>
      <table class="border-separate">
        <thead>
        <tr>
          <th>Year</th>
          <th>Event</th>
          <th>Description</th>
        </tr>
        </thead>
        <tbody>
        <tr>
          <td>2021-2024</td>
          <td>University - Master</td>
          <td>
            From 2021 I was pursuing my <i>Master of Science in Computer Science</i> with a focus on
            <i>IT-Security</i> at the University of Hamburg.
            I concluded my studies with the thesis <i>Security Evaluation and Vulnerability Assessment of
            FlatBuffers</i> (<a href="/static/assets/master_thesis_lilly_sell.pdf" target="_blank">Master-Thesis
            Download</a>) in the later half of 2024.
          </td>
        </tr>

        <tr>
          <td>2022-2024</td>
          <td>Working Student at <a href="https://vivaconagua.org" rel="external">Viva con Agua</a></td>
          <td>
            I was employed at <i>Viva con Agua</i> where I was in charge of operating their servers
            and deployment processes. Typical SysAdmin & DevOps work.
          </td>
        </tr>

        <tr>
          <td>2021-2022</td>
          <td>SHK at TAMS (University of Hamburg)</td>
          <td>
            During this period I was employed as a student tutor teaching the
            <i>Robocup Projekt</i> and <i>Robocup Praktikum</i> courses.
          </td>
        </tr>

        <tr>
          <td>2017-2021</td>
          <td>University - Bachelor</td>
          <td>
            I have finished my <i>Bachelor of Science in Computer Science</i> degree in 2021 with
            my final thesis about the
            <i>Integration of Software Development Testing Practices in Robotics</i> (<a
              href="/static/assets/bachelor_thesis_finn_sell.pdf" target="_blank">BA-Thesis Download</a>).
          </td>
        </tr>
        <tr>
          <td>2019-2020</td>
          <td>
            Working student at
            <a href="https://assessment.aon.com/en-us/" target="_blank" rel="external">AON Assessment
              Solutions</a>
          </td>
          <td>
            At AON I was tasked with multiple software development tasks including the creation
            and evaluation of a browser-based frontend testing solution.
          </td>
        </tr>
        <tr>
          <td>2018-2019</td>
          <td>SHK at Softwaretechnik (University of Hamburg)</td>
          <td>
            I was employed as student tutor tasked with supporting new students to learn basic
            programming principles and the Java programming language.
          </td>
        </tr>
        <tr>
          <td>2018-2018</td>
          <td>SHK at Sicherheit in verteilten Systemen (University of Hamburg)</td>
          <td>
            At SVS I was part of a team developing a system used for storing and processing
            medical information. My tasks mostly consisted of implementing and managing the
            Continuous Integration environment.
          </td>
        </tr>
        <tr>
          <td>2015</td>
          <td>
            Internship at
            <a href="https://www.popp-feinkost.de/" target="_blank" rel="external">
              Popp Feinkost GmbH</a>
          </td>
          <td>
            This internship was one of the first steps into an IT oriented career at which I was
            part of Popp's internal IT-Department.<br/>
            My work there consisted of helping out in maintaining the company infrastructure,
            refilling printer toner (of course) and automating small tasks with Excel Macros.
          </td>
        </tr>
        <tr>
          <td>2014</td>
          <td>Year abroad in Canada</td>
          <td>
            I originally went to Canada to improve my english skill (which worked) and got a
            second family in the process. We're still in close contact and have met again a few
            times over the past years.
          </td>
        </tr>
        <tr>
          <td>2013</td>
          <td>
            Internship at
            <a href="https://www.lufthansa-technik.com/" target="_blank" rel="external">
              Lufthansa Technik AG</a>
          </td>
          <td>
            During this internship I helped disassembling and assembling aircraft engines when
            they underwent maintenance in Hamburg.<br/>
            It was more of a manual labor type job; quite different from what I do now which
            didn't make it any less interesting though and I enjoyed it a lot.
          </td>
        </tr>
        <tr>
          <td>2008-2017</td>
          <td>Highschool</td>
          <td>
            I went to <i>Elsensee Gymnasium</i> in Quickborn until grade 11 at which point I did
            my year abroad in Canada. Afterwards I continued my education at
            <i>Berufsbildungszentrum Norderstedt</i> where I graduated with <i>Abitur</i> in 2017.
          </td>
        </tr>
        </tbody>
      </table>
    </section>
  </HCommand>
</template>

<style scoped>
@reference "~/assets/css/main.css";

p {
  @apply my-2;
}

th,td {
  @apply border-1 border-black2 px-2 py-2 m-1;
}
</style>
