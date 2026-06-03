---
search:
  boost: 10.0
---

# Class: SocialMedia 


_Information about social media_



<div data-search-exclude markdown="1">



URI: [pd:SocialMedia](https://w3id.org/lmodel/dpv/pd/SocialMedia)





```mermaid
 classDiagram
    class SocialMedia
    click SocialMedia href "../SocialMedia/"
      Communication <|-- SocialMedia
        click Communication href "../Communication/"
      

      SocialMedia <|-- PubliclyAvailableSocialMedia
        click PubliclyAvailableSocialMedia href "../PubliclyAvailableSocialMedia/"
      

      
```





## Inheritance
* [Social](Social.md)
    * [Communication](Communication.md)
        * **SocialMedia**
            * [PubliclyAvailableSocialMedia](PubliclyAvailableSocialMedia.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:SocialMedia](https://w3id.org/lmodel/dpv/pd/SocialMedia) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Social Media




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#SocialMedia |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:SocialMedia |
| native | pd:SocialMedia |
| exact | dpv_pd:SocialMedia, dpv_pd_owl:SocialMedia |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SocialMedia
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#SocialMedia
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about social media
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Social Media
exact_mappings:
- dpv_pd:SocialMedia
- dpv_pd_owl:SocialMedia
is_a: Communication
class_uri: pd:SocialMedia

```
</details>

### Induced

<details>
```yaml
name: SocialMedia
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#SocialMedia
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about social media
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Social Media
exact_mappings:
- dpv_pd:SocialMedia
- dpv_pd_owl:SocialMedia
is_a: Communication
class_uri: pd:SocialMedia

```
</details></div>