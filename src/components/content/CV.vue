<template>
  <div>
    <h5>Introduction</h5>
    <p class="no-top-margin">
      Hello there I'm Finn-Thorben Sell.<br><br>
      I am currently pursuing my <i>Bachelor of Science in Computer Science</i> at
      the University of Hamburg.<br>
      My hobbies consist of playing Badminton, engaging in the
      <a href="https://bit-bots.de" target="_blank">Hamburg Bit-Bots</a> - a student organized
      RoboCup Team and
      doing my own Projects (like this Website).
    </p>

    <h5>Curriculum Vitae</h5>
    <table class="double-lined-table">
      <thead>
      <tr>
        <td>Year</td>
        <td>Event</td>
        <td>Description</td>
      </tr>
      </thead>
      <tbody>
      <tr>
        <td>2017-now</td>
        <td>University</td>
        <td>Since 2017 I am pursuing my <i>Bachelor of Science in Computer Science</i> at the
          University of Hamburg
        </td>
      </tr>
      <tr>
        <td>2019-now</td>
        <td>Working student at <a href="https://assessment.aon.com/en-us/">AON Assessment
          Solutions</a></td>
        <td>
          At AON I am tasked with multiple software development tasks including the evaluation of a
          browser-based
          frontend testing framework.
        </td>
      </tr>
      <tr>
        <td>2018-2019</td>
        <td>Studentische Hilfskraft at Softwaretechnik (University of Hamburg)</td>
        <td>
          I was employed as student-tutor meaning that I supported new students in learning basic
          programming principles and the Java programming language.
        </td>
      </tr>
      <tr>
        <td>2018-2018</td>
        <td>Studentische Hilfskraft at Sicherheit in verteilten Systemen (University of Hamburg)
        </td>
        <td>
          At SVS I was part of a team developing a system used for storing and processing medical
          information.
          My tasks mostly consisted of implementing and managing the Continuous Integration
          environment.
        </td>
      </tr>
      <tr>
        <td>2015</td>
        <td>
          Internship at <a href="https://www.popp-feinkost.de/" target="_blank" class="simple-link">
          Popp Feinkost GmbH</a>
        </td>
        <td>
          This internship was one of the first steps into an IT oriented career at which I was part
          of Popp's
          internal IT-Department.<br>
          My work there consisted of helping out in maintaining the company infrastructure,
          refilling printer toner
          (of course) and automating small tasks with Excel Macros.
        </td>
      </tr>
      <tr>
        <td>2014</td>
        <td>Year abroad in Canada</td>
        <td>
          I originally went to Canada to improve my english skill (which worked) and got a second
          family in the
          process. We're still in close contact and have met again a few times over the past years.
        </td>
      </tr>
      <tr>
        <td>2013</td>
        <td>
          Internship at <a href="https://www.lufthansa-technik.com/" target="_blank"
                           class="simple-link">
          Lufthansa Technik AG</a>
        </td>
        <td>
          During this internship I helped disassembling and assembling aircraft engines when they
          underwent
          maintenance in Hamburg.<br>
          It was more of a manual labor type job; quite different from what I do now which didn't
          make it any
          less interesting though and I enjoyed it a lot.
        </td>
      </tr>
      <tr>
        <td>2008-2017</td>
        <td>Highschool</td>
        <td>
          I went to <i>Elsensee Gymnasium</i> in Quickborn until grade 11 at which point I did my
          year abroad
          in Canada. Afterwards I continued my education at <i>Berufsbildungszentrum Norderstedt</i>
          where I
          graduated with <i>Abitur</i> in 2017.
        </td>
      </tr>
      <tr>
        <td>2004-2008</td>
        <td>Primary School</td>
        <td>My Primary School was the <i>Lakwegschule</i> in Kaltenkirchen</td>
      </tr>
      <tr>
        <td>1998</td>
        <td>Birth</td>
        <td></td>
      </tr>
      </tbody>
    </table>

  </div>
</template>

<script lang="ts">
  import Vue from 'vue';
  import Component from 'vue-class-component';
  import 'vue-class-component/hooks';
  import {Prop} from 'vue-property-decorator';
  import VueTypes from 'vue-types';

  @Component({})
  export default class CV extends Vue {
  }
</script>

<style scoped lang="scss">
  @use "src/styles/colors";

  h5:first-of-type {
    margin-top: 0;
  }

  h5 {
    margin-bottom: 15px;
  }

  table.double-lined-table, table.double-lined-table td {
    border: 1px solid colors.get-color("grey");
  }
  td {
    padding: 8px;
  }
</style>
