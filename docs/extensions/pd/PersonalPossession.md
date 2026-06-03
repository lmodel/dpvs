---
search:
  boost: 10.0
---

# Class: PersonalPossession 


_Information about personal possessions_



<div data-search-exclude markdown="1">



URI: [pd:PersonalPossession](https://w3id.org/lmodel/dpv/pd/PersonalPossession)





```mermaid
 classDiagram
    class PersonalPossession
    click PersonalPossession href "../PersonalPossession/"
      Ownership <|-- PersonalPossession
        click Ownership href "../Ownership/"
      
      
```





## Inheritance
* [Financial](Financial.md)
    * [Ownership](Ownership.md)
        * **PersonalPossession**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:PersonalPossession](https://w3id.org/lmodel/dpv/pd/PersonalPossession) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Personal Possession




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#PersonalPossession |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:PersonalPossession |
| native | pd:PersonalPossession |
| exact | dpv_pd:PersonalPossession, dpv_pd_owl:PersonalPossession |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PersonalPossession
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#PersonalPossession
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about personal possessions
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Personal Possession
exact_mappings:
- dpv_pd:PersonalPossession
- dpv_pd_owl:PersonalPossession
is_a: Ownership
class_uri: pd:PersonalPossession

```
</details>

### Induced

<details>
```yaml
name: PersonalPossession
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#PersonalPossession
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about personal possessions
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Personal Possession
exact_mappings:
- dpv_pd:PersonalPossession
- dpv_pd_owl:PersonalPossession
is_a: Ownership
class_uri: pd:PersonalPossession

```
</details></div>