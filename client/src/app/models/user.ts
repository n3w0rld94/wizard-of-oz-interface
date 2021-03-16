export interface User {
    username: string;
    permissions: UserPermission;
}

export interface UserPermission {
    USE_TEST_API: boolean;
    USE_DEVELOPER_TOOLS: boolean;
}
