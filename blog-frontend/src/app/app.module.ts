import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { BlogPostsComponent } from './blog-posts/blog-posts.component';
import { BlogApiService } from './blog-api.service';
import { PaginationComponent } from './pagination/pagination.component';
import { FilteringComponent } from './filtering/filtering.component';
import { SortingComponent } from './sorting/sorting.component';

@NgModule({
  declarations: [
    AppComponent,
    BlogPostsComponent,
    PaginationComponent,
    FilteringComponent,
    SortingComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule
  ],
  providers: [BlogApiService],
  bootstrap: [AppComponent]
})
export class AppModule { }
