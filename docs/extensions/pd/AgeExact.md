---
search:
  boost: 10.0
---

# Class: AgeExact 


_Information about the exact age (i.e. to some degree within a year,_

_month, or day)_



<div data-search-exclude markdown="1">



URI: [pd:AgeExact](https://w3id.org/lmodel/dpv/pd/AgeExact)





```mermaid
 classDiagram
    class AgeExact
    click AgeExact href "../AgeExact/"
      AgeRange <|-- AgeExact
        click AgeRange href "../AgeRange/"
      
      
```





## Inheritance
* [External](External.md)
    * [PhysicalCharacteristic](PhysicalCharacteristic.md)
        * [Age](Age.md)
            * [AgeRange](AgeRange.md)
                * **AgeExact**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:AgeExact](https://w3id.org/lmodel/dpv/pd/AgeExact) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Age Exact




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#AgeExact |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:AgeExact |
| native | pd:AgeExact |
| exact | dpv_pd:AgeExact, dpv_pd_owl:AgeExact |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AgeExact
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#AgeExact
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about the exact age (i.e. to some degree within a year,

  month, or day)'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Age Exact
exact_mappings:
- dpv_pd:AgeExact
- dpv_pd_owl:AgeExact
is_a: AgeRange
class_uri: pd:AgeExact

```
</details>

### Induced

<details>
```yaml
name: AgeExact
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#AgeExact
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about the exact age (i.e. to some degree within a year,

  month, or day)'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Age Exact
exact_mappings:
- dpv_pd:AgeExact
- dpv_pd_owl:AgeExact
is_a: AgeRange
class_uri: pd:AgeExact

```
</details></div>