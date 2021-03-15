export interface AnimusRobot {
    joinDate: string;
    license: AnimusRobotLicese;
    make: string;
    model: string;
    name: string;
    robotConfig: AnimusRobotConfig;
    robotId: string;
    robotState: AnimusRobotState;
}

interface AnimusRobotLicese {
    licenseId: string;
    startDate: string;
    endDate: string;
    duration: string;
}

interface AnimusRobotConfig {
    StrAudioParams: AnimusRobotAudioParameters;
    inputModalities: string[];
    outputModalities: string[];
    enableRemote: boolean;
}

interface AnimusRobotState {
    NetworkMode: string;
    location: AnimusRobotLocation;
}

interface AnimusRobotAudioParameters {
    Backends: string[];
    Channel: number;
    SampleRate: number;
    SizeInFrames: boolean;
    TransmitRate: number;
}

interface AnimusRobotLocation {
    city: string;
    country: string;
    ip: string;
    loc: string;
    org: string;
    postal: string;
    region: string;
}