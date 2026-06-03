---
search:
  boost: 10.0
---

# Class: Picture 


_Information about visual representation or image e.g. profile photo_



<div data-search-exclude markdown="1">



URI: [pd:Picture](https://w3id.org/lmodel/dpv/pd/Picture)





```mermaid
 classDiagram
    class Picture
    click Picture href "../Picture/"
      Identifying <|-- Picture
        click Identifying href "../Identifying/"
      
      
```





## Inheritance
* [External](External.md)
    * [Identifying](Identifying.md)
        * **Picture**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Picture](https://w3id.org/lmodel/dpv/pd/Picture) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Picture




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Picture |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Picture |
| native | pd:Picture |
| exact | dpv_pd:Picture, dpv_pd_owl:Picture |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Picture
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Picture
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about visual representation or image e.g. profile photo
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Picture
exact_mappings:
- dpv_pd:Picture
- dpv_pd_owl:Picture
is_a: Identifying
class_uri: pd:Picture

```
</details>

### Induced

<details>
```yaml
name: Picture
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Picture
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about visual representation or image e.g. profile photo
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Picture
exact_mappings:
- dpv_pd:Picture
- dpv_pd_owl:Picture
is_a: Identifying
class_uri: pd:Picture

```
</details></div>