<script lang="ts">
	import { T } from '@threlte/core';
	import { Sky } from 'three/addons/objects/Sky.js';
	import { Vector3 } from 'three';

	const sunPosition = new Vector3(.25,.15,.25)

	const sky = new Sky();
	sky.scale.setScalar(450000);
	sky.material.uniforms['sunPosition'].value = sunPosition;
</script>

<T.DirectionalLight castShadow={true} position={sunPosition.toArray()}/>
<T is={sky} />
<T.AmbientLight />