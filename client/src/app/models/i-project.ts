import { AnimusRobot } from './animus-robot';

export interface IProject {
    title: string;
    description: string;
    supportedRobots: AnimusRobot[];
    supportedRobotsText?: string;
    user?: string;
}
