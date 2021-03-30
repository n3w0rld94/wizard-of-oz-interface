import { AnimusRobot } from './animus-robot';
import { IProject } from './i-project';
import { User } from './user';

type ValidPayload =
    GetRobotsResponse |
    User |
    IProject |
    IProject[];

export interface AnimusServerResponse<T extends ValidPayload> extends AnimusBaseServerResponse {
    payload?: T;
}

export interface AnimusBaseServerResponse {
    success: boolean;
    description: string;
    code: number;
}

export interface GetRobotsResponse {
    robots: AnimusRobot[];
    errors: AnimusBaseServerResponse[];
}
