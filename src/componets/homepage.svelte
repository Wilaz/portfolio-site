<script lang="ts">
  	import { onMount } from 'svelte';
	import { T, useThrelte, useTask } from '@threlte/core';
	import { Vector3, CatmullRomCurve3 } from 'three';
	import Sky from '@componets/sky.svelte';
	import Diorama from '@models/diorama.svelte';
	import Text from '@models/text.svelte';
	const { camera } = useThrelte();

	let scrollAmount: number = $state(0);
	const pageHeight: number = 1600;

	const spline = new CatmullRomCurve3([
		new Vector3(1.3, -.7, -2.5),
		new Vector3(1, -1.2, 0),
		new Vector3(1, -1.8, 1.5)
	]);

	function clamp(min, x, max) {
		return Math.min(Math.max(x, min), max);
	};

  	// Handles moving
  	const handleScroll = (event: WheelEvent) => {
		scrollAmount = clamp(0, scrollAmount + event.deltaY / pageHeight, 1);
	};

	onMount(() => {
		window.addEventListener('wheel', handleScroll);
		return () => {
			window.removeEventListener('wheel', handleScroll);
		};
	});

	function moveCameraAlongSpline() {
		const point = spline.getPointAt(scrollAmount);
		$camera.position.set(point.x, point.y, point.z);
		$camera.lookAt(new Vector3(1, -1.8, 2.5))
	};

	useTask(() => {
		moveCameraAlongSpline();
	})
</script>

<T.PerspectiveCamera
	fov={60}
	near={.1}
	far={20000}
	makeDefault
/>

<Sky />

<Diorama />

<T.Group position={[1.7, -1.8, 2.5]}>
	<Text />
</T.Group>