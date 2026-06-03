---
search:
  boost: 10.0
---

# Class: IndividualProfile 


_Individual profile or user profile is information and representation of_

_characteristics associated with a specific individual_



<div data-search-exclude markdown="1">



URI: [pd:IndividualProfile](https://w3id.org/lmodel/dpv/pd/IndividualProfile)





```mermaid
 classDiagram
    class IndividualProfile
    click IndividualProfile href "../IndividualProfile/"
      Profile <|-- IndividualProfile
        click Profile href "../Profile/"
      
      
```





## Inheritance
* [Profile](Profile.md)
    * **IndividualProfile**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:IndividualProfile](https://w3id.org/lmodel/dpv/pd/IndividualProfile) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Individual Profile




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#IndividualProfile |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:IndividualProfile |
| native | pd:IndividualProfile |
| exact | dpv_pd:IndividualProfile, dpv_pd_owl:IndividualProfile |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IndividualProfile
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#IndividualProfile
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Individual profile or user profile is information and representation
  of

  characteristics associated with a specific individual'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Individual Profile
exact_mappings:
- dpv_pd:IndividualProfile
- dpv_pd_owl:IndividualProfile
is_a: Profile
class_uri: pd:IndividualProfile

```
</details>

### Induced

<details>
```yaml
name: IndividualProfile
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#IndividualProfile
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Individual profile or user profile is information and representation
  of

  characteristics associated with a specific individual'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Individual Profile
exact_mappings:
- dpv_pd:IndividualProfile
- dpv_pd_owl:IndividualProfile
is_a: Profile
class_uri: pd:IndividualProfile

```
</details></div>