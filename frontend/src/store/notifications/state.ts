import { INotification } from "@/interfaces";

export interface NotificationState {
  notifications: INotification[];
  notificationsUnread: Number | 0;
}
