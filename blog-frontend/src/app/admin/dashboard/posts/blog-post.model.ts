export interface BlogPost {
  id: number;
  title: string;
  content: string;
  author: string,
  created_at: Date | string;
  updated_at: Date | string;
}
