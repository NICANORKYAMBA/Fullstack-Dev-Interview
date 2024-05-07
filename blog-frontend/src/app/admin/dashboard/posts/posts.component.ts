import { Component, OnInit } from "@angular/core";
import { BlogPost } from './blog-post.model';
import { BlogApiService } from './blog-api.service';

@Component({
  selector: 'app-posts',
  templateUrl: './posts.component.html',
  styleUrls: ['./posts.component.scss']
})
export class PostComponent implements OnInit {
  blogPosts: BlogPost[] = [];
  currentPage: number = 1;
  pageSize: number = 10;
  totalPages: number = 0;
  filters: any = {};
  sort: string = '';

  constructor(private blogApiService: BlogApiService) { }

  ngOnInit(): void {
    this.getBlogPosts();
  }

  getBlogPosts() {
    this.blogApiService.getBlogPosts(this.currentPage, this.pageSize, this.filters, this.sort)
      .subscribe(data => {
        this.blogPosts = data;
        this.totalPages = Math.ceil(data.length / this.pageSize);
      }, error => {
        console.error('Error fetching blog posts:', error);
        throw new Error('Failed to fetch blog posts. Check your internet connection or backend service.');
      });
  }

  changePage(page: number) {
    this.currentPage = page;
    this.getBlogPosts();
  }

  changePageSize(size: number) {
    this.pageSize = size;
    this.currentPage = 1;
    this.getBlogPosts();
  }

  filterPosts(filters: any) {
    this.filters = filters;
    this.currentPage = 1;
    this.getBlogPosts();
  }

  sortPosts(sort: string) {
    this.sort = sort;
    this.currentPage = 1;
    this.getBlogPosts();
  }
}
