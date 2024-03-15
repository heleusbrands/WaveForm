Dial {
	id: dial
	x: 334
	y: 278
	width: 234
	height: 234
	z: 1
	clip: true
	background: Item {
		width: parent.width
		height: parent.height
		Rectangle {
			anchors.fill: parent
			z: -1
			clip: true
			gradient: gradient1
		}
	}
	ShaderEffectSource {
		id: dialClip
		sourceItem: dial
		width: dial.width
		height: dial.height
		visible: false
	}
	onVisibleChanged: {
		dialClip.visible = visible
	}
}

RadialGradient {
	id: gradient1
	centerX: dial.width / 2
	centerY: dial.height / 2
	radius: Math.min(dial.width, dial.height) / 2
	focalX: centerX
	focalY: centerY
	GradientStop { position: 0; color: "blue" }
	GradientStop { position: 0.2; color: "green" }
	GradientStop { position: 0.4; color: "red" }
	GradientStop { position: 0.6; color: "yellow" }
	GradientStop { position: 1; color: "cyan" }
	clip: true
	source: dialClip
}