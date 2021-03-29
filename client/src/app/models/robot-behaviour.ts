import { RobotModality } from './robot-modalities';

export class RobotBehaviour {
    private $behaviourType: RobotModality;
    private $modalityName: string;
    name: string;
    payload: any;
    behaviours?: RobotBehaviour[];

    get behaviourType() {
        return this.$behaviourType || '';
    }

    set behaviourType(behaviourType: RobotModality) {
        this.$behaviourType = behaviourType;
    }

    get modalityName() {
        return this.$modalityName || '';
    }
}
