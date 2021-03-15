import { Type } from '@angular/core';
import { AnimusRobot } from './animus-robot';

type ValidPayload = GetRobotsResponse;

export interface AnimusServerResponse<T extends ValidPayload> extends AnimusBaseServerResponse {
    payload: T;
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
