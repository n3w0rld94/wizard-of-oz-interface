export interface User {
    name: string;
    username: string;
    permissions: UserPermission;
}

export interface UserPermission {
    USE_TEST_API: boolean;
    USE_DEVELOPER_TOOLS: boolean;
}
