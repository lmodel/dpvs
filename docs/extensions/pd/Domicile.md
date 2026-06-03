---
search:
  boost: 10.0
---

# Class: Domicile 


_Information about domicile status e.g. which region or country a person_

_is domiciled in_



<div data-search-exclude markdown="1">



URI: [pd:Domicile](https://w3id.org/lmodel/dpv/pd/Domicile)





```mermaid
 classDiagram
    class Domicile
    click Domicile href "../Domicile/"
      DpvLocation <|-- Domicile
        click DpvLocation href "../DpvLocation/"
      
      
```





## Inheritance
* [Tracking](Tracking.md)
    * [DpvLocation](DpvLocation.md)
        * **Domicile**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Domicile](https://w3id.org/lmodel/dpv/pd/Domicile) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Domicile


## Comments

* Parent changed to pd:Location



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Domicile |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Domicile |
| native | pd:Domicile |
| exact | dpv_pd:Domicile, dpv_pd_owl:Domicile |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Domicile
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Domicile
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about domicile status e.g. which region or country a person

  is domiciled in'
comments:
- Parent changed to pd:Location
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Domicile
exact_mappings:
- dpv_pd:Domicile
- dpv_pd_owl:Domicile
is_a: DpvLocation
class_uri: pd:Domicile

```
</details>

### Induced

<details>
```yaml
name: Domicile
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Domicile
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about domicile status e.g. which region or country a person

  is domiciled in'
comments:
- Parent changed to pd:Location
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Domicile
exact_mappings:
- dpv_pd:Domicile
- dpv_pd_owl:Domicile
is_a: DpvLocation
class_uri: pd:Domicile

```
</details></div>