class Animus_Audio_Params:
    """ #### Interface to the Animus Audio Parameters
        #### Attributes:
                `Backends (list)`: Can be a list of any of the following values:
                    ["alsa", "wasapi", "dsound", "winmm", "pulse", "jack", "coreaudio", "sndio", "audio4", "oss", "opensl", "openal", "sdl"]
                `SampleRate (int)`: Samples transmitted per second.
                `Channels (int)`: No idea seriously, leave to 1.
                `SizeInFrames (bool)`: no idea again, author suggests to leave this to true.
                `TransmitRate (int)`: Packets per second.
    """
    
    Backends: list
    SampleRate: int
    Channels: int
    SizeInFrames: bool
    TransmitRate: int