<script lang="ts">
  	import { onMount } from 'svelte';
	import { T, useThrelte, useTask } from '@threlte/core';
	import { Vector3, CatmullRomCurve3 } from 'three';
	const { camera } = useThrelte();
	import Sky from '@componets/sky.svelte';
	import Diorama from '@models/diorama.svelte';

	let scrollAmount: number = $state(0);
	const pageHeight: number = 1600;

	const spline = new CatmullRomCurve3([
		new Vector3(0, 1, 0),
		new Vector3(0, 1, 1),
		new Vector3(1, 1, 0)
	]);

	function clamp(min, x, max) {
		return Math.min(Math.max(x, min), max);
	};

  	// Handles moving
  	const handleScroll = (event: WheelEvent) => {
		scrollAmount = clamp(0, scrollAmount + event.deltaY / pageHeight, .99);
	};

	onMount(() => {
		window.addEventListener('wheel', handleScroll);
		return () => {
			window.removeEventListener('wheel', handleScroll);
		};
	});

	function moveCameraAlongSpline() {
		const point = spline.getPointAt(scrollAmount);
		const rot = spline.getPointAt(scrollAmount + 0.01);
		$camera.position.set(point.x, point.y, point.z);
		$camera.lookAt(rot)
	};

	useTask(() => {
		moveCameraAlongSpline();
	})
</script>

<T.PerspectiveCamera
	fov={60}
	near={1}
	far={20000}
	makeDefault
/>

<Sky />

<Diorama />