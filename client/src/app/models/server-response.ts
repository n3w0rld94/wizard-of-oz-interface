import { AnimusRobot } from './animus-robot';
import { User } from './user';

type ValidPayload =
    GetRobotsResponse |
    User;

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
