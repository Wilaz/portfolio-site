<script lang="ts">
	import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
	import { useLoader, T } from '@threlte/core';

	const gltf = useLoader(GLTFLoader).load('/src/models/text.glb');
</script>

{#if $gltf}
	<T is={$gltf.scene} rotation={[-Math.PI/2, Math.PI, 0]} scale={.2}/>
{/if}
