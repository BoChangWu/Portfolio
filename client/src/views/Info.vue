<template>
  <div class="info">
    <Info1/>
    <Info2 />
  </div>
</template>

<script>
// @ is an alias to /src
import Info1 from '@/components/Info1.vue'
import Info2 from '@/components/Info2.vue'

export default {
  name: 'info',
  components: {
    Info1,
    Info2
  }
}
</script>

