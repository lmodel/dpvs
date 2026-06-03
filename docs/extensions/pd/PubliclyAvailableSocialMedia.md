---
search:
  boost: 10.0
---

# Class: PubliclyAvailableSocialMedia 


_Information about social media that is publicly available_



<div data-search-exclude markdown="1">



URI: [pd:PubliclyAvailableSocialMedia](https://w3id.org/lmodel/dpv/pd/PubliclyAvailableSocialMedia)





```mermaid
 classDiagram
    class PubliclyAvailableSocialMedia
    click PubliclyAvailableSocialMedia href "../PubliclyAvailableSocialMedia/"
      SocialMedia <|-- PubliclyAvailableSocialMedia
        click SocialMedia href "../SocialMedia/"
      
      
```





## Inheritance
* [Social](Social.md)
    * [Communication](Communication.md)
        * [SocialMedia](SocialMedia.md)
            * **PubliclyAvailableSocialMedia**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:PubliclyAvailableSocialMedia](https://w3id.org/lmodel/dpv/pd/PubliclyAvailableSocialMedia) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Publicly Available Social Media




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#PubliclyAvailableSocialMedia |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:PubliclyAvailableSocialMedia |
| native | pd:PubliclyAvailableSocialMedia |
| exact | dpv_pd:PubliclyAvailableSocialMedia, dpv_pd_owl:PubliclyAvailableSocialMedia |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PubliclyAvailableSocialMedia
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#PubliclyAvailableSocialMedia
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about social media that is publicly available
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Publicly Available Social Media
exact_mappings:
- dpv_pd:PubliclyAvailableSocialMedia
- dpv_pd_owl:PubliclyAvailableSocialMedia
is_a: SocialMedia
class_uri: pd:PubliclyAvailableSocialMedia

```
</details>

### Induced

<details>
```yaml
name: PubliclyAvailableSocialMedia
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#PubliclyAvailableSocialMedia
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about social media that is publicly available
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Publicly Available Social Media
exact_mappings:
- dpv_pd:PubliclyAvailableSocialMedia
- dpv_pd_owl:PubliclyAvailableSocialMedia
is_a: SocialMedia
class_uri: pd:PubliclyAvailableSocialMedia

```
</details></div>