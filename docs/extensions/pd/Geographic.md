---
search:
  boost: 10.0
---

# Class: Geographic 


_Information about location or based on geography (e.g. home address)_



<div data-search-exclude markdown="1">



URI: [pd:Geographic](https://w3id.org/lmodel/dpv/pd/Geographic)





```mermaid
 classDiagram
    class Geographic
    click Geographic href "../Geographic/"
      Demographic <|-- Geographic
        click Demographic href "../Demographic/"
      
      
```





## Inheritance
* [External](External.md)
    * [Demographic](Demographic.md)
        * **Geographic**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Geographic](https://w3id.org/lmodel/dpv/pd/Geographic) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Geographic




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Geographic |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Geographic |
| native | pd:Geographic |
| exact | dpv_pd:Geographic, dpv_pd_owl:Geographic |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Geographic
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Geographic
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about location or based on geography (e.g. home address)
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Geographic
exact_mappings:
- dpv_pd:Geographic
- dpv_pd_owl:Geographic
is_a: Demographic
class_uri: pd:Geographic

```
</details>

### Induced

<details>
```yaml
name: Geographic
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Geographic
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about location or based on geography (e.g. home address)
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Geographic
exact_mappings:
- dpv_pd:Geographic
- dpv_pd_owl:Geographic
is_a: Demographic
class_uri: pd:Geographic

```
</details></div>