---
search:
  boost: 10.0
---

# Class: Like 


_Information about likes or preferences regarding attractions_



<div data-search-exclude markdown="1">



URI: [pd:Like](https://w3id.org/lmodel/dpv/pd/Like)





```mermaid
 classDiagram
    class Like
    click Like href "../Like/"
      Interest <|-- Like
        click Interest href "../Interest/"
      
      
```





## Inheritance
* [Internal](Internal.md)
    * [Preference](Preference.md)
        * [Interest](Interest.md)
            * **Like**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Like](https://w3id.org/lmodel/dpv/pd/Like) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Like




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Like |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Like |
| native | pd:Like |
| exact | dpv_pd:Like, dpv_pd_owl:Like |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Like
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Like
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about likes or preferences regarding attractions
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Like
exact_mappings:
- dpv_pd:Like
- dpv_pd_owl:Like
is_a: Interest
class_uri: pd:Like

```
</details>

### Induced

<details>
```yaml
name: Like
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Like
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about likes or preferences regarding attractions
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Like
exact_mappings:
- dpv_pd:Like
- dpv_pd_owl:Like
is_a: Interest
class_uri: pd:Like

```
</details></div>