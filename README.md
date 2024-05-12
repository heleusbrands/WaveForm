## WaveForm

by Bloom Research

---

#### Overview

The idea behind WaveForm was born during an audio research project, and out of a frustration with having to constantly reform, or reformat audio while passing it between tools. Each library has their own set of parameters needed to utilize the audio, and though almost all are capable of reading audio from the disk, once it's loaded into memory, the audio formatting parameters are constantly getting re-retrieved in order to pass to a new tool.

In addition, there don't seem to be many audio libraries, if any, that provide access to a _truly_ complete set of audio processing and analysis tools. As someone who comes from an audio engineering/processing background, this was frustrating.

Enter WaveForm. A high-level, yet advanced library, to allow for easy loading, formatting, reformatting, transformations, analysis, and more. It's a high-level multi-package wrapper, as well as a unified framework that includes many of it's own additions. It was designed in a way to make it quick, intuitive, and easy to use, as well as easily extendable. Right now, the core features are present, however expect many large updates in the future with more tools.

The Documentation is a work in progress. Will update when it's available. However, I generally try to document important things as I go.

_**Note:** the library is still under construction, and will eventually include a direct interface and full access to several C# libraries that are currently unavailable in python. Right now, the only C# interface included is to the **'RubberBand'** library, which will eventually be made available as it's own separate package. However, soon the library will also include a full-featured interface to the **'NWave'** C# library as well. The library's construction is almost complete, after which it will just need to be tested._

#### Quick Start

```python
from waveform import WaveForm

wf = WaveForm('audio_file.wav')

# Create a new form
array = wf.forms.numpy_array # Numpy Array Access
tensor = wf.forms.tensor # Tensorflow Tensor Access
sound = wf.forms.sound # ParselMouth Sound Access
audio_segment = wf.forms.audio_segment # Pydub AudioSegment Access
byte = wf.forms.byte # Pure Bytes Access
# Quick Info View
print(wf.info)

"""
FormReportConfig(
    duration=0.4676666666666667,
    max=14088.0,
    dBFS=-21.459403317905384,
    max_dBFS=-7.332011840009947,
    rms=2770.0,
    array_type=None)
"""

# Get Pitch Information via the pitch Informer
wf.informers.pitch.dataframe
```

| idx | time      | frequency | decibel  | frame |
| --- | --------- | --------- | -------- | ----- |
| 0   | 0.0208333 | 284.54    | 0.65828  | 1000  |
| 1   | 0.0228333 | 293.595   | 0.673344 | 1096  |
| 2   | 0.0248333 | 251.864   | 0.684609 | 1192  |
| 3   | 0.0268333 | 251.762   | 0.700551 | 1288  |
| ... | ...       | ...       | ...      | ...   |

### Architecture

---

#### Mechanism

> Underneath the public-facing structure of the class, WaveForm stores audio as an array, as well as it's parameters (much like pydub's AudioSegment). It then employs specialized Form subclasses to pass the array and audio parameters to various objects. This allows different forms to be easily available on-demand, without having to re-access or keep track of the initial parameters.
>
> Forms, Informers, and Reformers are all passed the base WaveForm class when they are created, allowing them to access the audio information as well as update any necessary elements, without having to create a new object.

#### Audio Loading

> WaveForm tries to make loading audio as simple as possible, by accepting any of the forms available as input, and requiring as few parameters as possible. In the instance that certain parameters are missing, it will attempt to analyze the audio structure to extract or guess the parameters where possible.

#### Design

> Generally, WaveForm tries to make navigation and endpoints easy to browse and access, without a ton of memory overhead, by taking a unique approach through the utilization of class parameters. For example:

```python
wf.forms.form_analysis
# -> AnalysisGrid()
```

#### Args vs Settings

> Because many of the functions/classes have complex and long list of parameters, many of which are not required and have solid base defaults, I decided to take a different approach by wrapping complex functions in a Class with a `settings` attribute, making configuration and browsing parameters easy. For example, when you access the Intensity Reformer's settings, which can be done through:

```python
wf.reformers.intensity.settings
```

> ... you are actually accessing:

```python
wf.forms.form_analysis.settings.Intensity

"""
_Intensity(
    min_frequency=100.0,
    time_step=0.002,
    subtract_mean_pressure=True
    )
"""
```

> ... meaning that settings can be adjusted in the following format:

```python
wf.reformers.intensity.settings.min_frequency = 50
```

> _Note: this is a minimal example of the format, however some classes have around 10 different settings that can be adjusted._

### Forms

> Forms represent a object or format for the audio to take (i.e. the form that you want it to take). When a new form is created by accessing the appropriate parameter, it is both returned by the parameter (allowing for assignment to a variable if desired), as well as assigned as the `audio` attribute of the base WaveForm class (allowing for you to continue working with the audio in that form, until you need to switch it to a new one). While the `audio` attribute is reassigned with each new form, the underlying data remains in it's array form.
>
> The included forms will be continually expanded, but for now the following forms are available:

- audio_segment: pydub.AudioSegment
- sound: parselmouth.Sound
- audio_file: File
- tensor: tensorflow.Tensor
- numpy_array: numpy.ndarray
- byte: bytes

### Reformers

> Reformers represent a Transformation to a WaveForm (i.e. something that modifies the original audio). `Form` changes happen in-place, whereas `Reformer` changes return a new WaveForm instance with the modified audio. This is done to allow for the preservation of the original, for example in the instance of audio experimentation/analysis. Eventually a in-place property setting will be added to base Reformer class, to allow for the changing of this behavior if desired.

> Reformers tend to make heavy utilization of the `settings` property to adjust the list of available parameters.

> Most Reformers' primary functions can be activated using the call method of the Reformer subclass. With this workflow, the settings can be adjusted as needed before the transformation is applied. However, in the case of more complex Reformer's, additional methods may be made available, changing the type/mechanics of the transformation. For example:

```python
wf.reformers.flux.warp_to_match(wf2) # Let's you warp WaveForm to match WaveForm2
```

> In addition, there are some Reformers where commonly accessed settings are made available as direct properties of the subclass, as well as within the Reformer's `settings` property. For example, the `ReformFlux` reformer is a pitch warping transformation that utilizes the `tsm` module. The module has several algorithms made available to accomplish the task, and so these algorithms are made even more easily accessible via the property shortcuts. For example:

```python
wf.reformers.flux.use_wsola # Sets the wsola algorithm
```

> ... is a shorthand for:

```python
wf.reformers.flux.settings.Algorithm = wf.reformers.flux.settings.algorithms.wsola
```

### Informers

> Informers represent an information extraction process. Informers have, at the very least, a `dataframe` parameter, which returns the results of the extraction process as a `pandas.Dataframe` object. Just as with `Reformers`, `Informers` will proceed with the extraction when the class is called, allowing for the settings to be adjusted first via the `settings` parameter. Calling the `dataframe` property will also activate the extraction _if_ the features have not already been extracted. So note here that if you adjust the settings after the first call, you'll need to directly call the class to update features. _This will likely be adjusted and optimized in the future, to automatically detect when settings have changed and then perform a re-call to update it's stored features._

> As of right now, there is only one informer made available via the WaveForm class, however many more will soon be added, and for the more experienced and tenacious user, most of the functionalities that will eventually added as Informers is already available and functional within the `WaveForm.audio_modules.extraction` module.

_**Please note that this project is still in early development, and is not recommended for production use yet. Much of the eventual functionality is built, but still needs to be wrapped and integrated into the high-level portion of the library for easy access.**_

#### C# Interfaces

> There are several C# audio libraries that I have wrapped for integration into this package, but will eventually also make available as standalone packages.

**Rubberband**

> _A direct and complete python interface to the Rubberband library had, to my knowledge, not been created yet. As someone who likes having access to all the options available, I thought I'd resolve this by creating an interface to the whole library._

- Development Status: **Initial Development Complete**
- Testing Status: **Initial Alpha Testing Complete**
- Integration Status: **Low-level Integration Complete**

**NWaves**

> _This is an amazing and quite extensive C# library, that will expand WaveForm's functionality significantly. However, because of it's size it's development is still in progress. Will update when it has been integrated._

- Development Status: **In-Progress**
- Testing Status: **In-Progress**
- Integration Status: **Not Integrated**
