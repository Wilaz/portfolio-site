<script lang="ts">
  	import { onMount } from 'svelte';
	import { T, useThrelte, useTask } from '@threlte/core';
	import { Vector3, CatmullRomCurve3 } from 'three';
	const { camera } = useThrelte();
	import Sky from '@componets/sky.svelte';
	import Beach from '../beach.svelte';

	let scrollAmount: number = $state(0);
	const pageHeight: number = 800;

	const spline = new CatmullRomCurve3([
		new Vector3(5, 0, 5),
		new Vector3(5, 0, -5),
		new Vector3(-5, 0, -5),
		new Vector3(-5, 0, 5)
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
		const origin = new Vector3(0,0,0)
		$camera.position.set(point.x, point.y, point.z);
		$camera.lookAt(origin)
	};

	useTask(() => {
		moveCameraAlongSpline();
	})
</script>

<T.Mesh >
	<T.TorusGeometry />
	<T.MeshStandardMaterial color="hotpink" />
</T.Mesh>

<T.PerspectiveCamera
	fov={60}
	near={1}
	far={20000}
	makeDefault
/>

<Sky />

<Beach />