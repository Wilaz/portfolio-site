<script lang="ts">

  import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
  import { useLoader, T } from '@threlte/core'

  const gltf = useLoader(GLTFLoader).load('/src/models/diorama.glb')

</script>

{#if $gltf}
  <T is={$gltf.scene} rotation={[0, Math.PI, 0]}/>
{/if}