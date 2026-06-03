---
search:
  boost: 10.0
---

# Class: Dislike 


_Information about dislikes or preferences regarding repulsions_



<div data-search-exclude markdown="1">



URI: [pd:Dislike](https://w3id.org/lmodel/dpv/pd/Dislike)





```mermaid
 classDiagram
    class Dislike
    click Dislike href "../Dislike/"
      Interest <|-- Dislike
        click Interest href "../Interest/"
      
      
```





## Inheritance
* [Internal](Internal.md)
    * [Preference](Preference.md)
        * [Interest](Interest.md)
            * **Dislike**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Dislike](https://w3id.org/lmodel/dpv/pd/Dislike) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Dislike




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Dislike |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Dislike |
| native | pd:Dislike |
| exact | dpv_pd:Dislike, dpv_pd_owl:Dislike |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Dislike
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Dislike
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about dislikes or preferences regarding repulsions
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Dislike
exact_mappings:
- dpv_pd:Dislike
- dpv_pd_owl:Dislike
is_a: Interest
class_uri: pd:Dislike

```
</details>

### Induced

<details>
```yaml
name: Dislike
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Dislike
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about dislikes or preferences regarding repulsions
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Dislike
exact_mappings:
- dpv_pd:Dislike
- dpv_pd_owl:Dislike
is_a: Interest
class_uri: pd:Dislike

```
</details></div>