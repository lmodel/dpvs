---
search:
  boost: 10.0
---

# Class: PublicLife 


_Information about public life_



<div data-search-exclude markdown="1">



URI: [pd:PublicLife](https://w3id.org/lmodel/dpv/pd/PublicLife)





```mermaid
 classDiagram
    class PublicLife
    click PublicLife href "../PublicLife/"
      Social <|-- PublicLife
        click Social href "../Social/"
      

      PublicLife <|-- Character
        click Character href "../Character/"
      PublicLife <|-- CommunicationsMetadata
        click CommunicationsMetadata href "../CommunicationsMetadata/"
      PublicLife <|-- GeneralReputation
        click GeneralReputation href "../GeneralReputation/"
      PublicLife <|-- Interaction
        click Interaction href "../Interaction/"
      PublicLife <|-- MaritalStatus
        click MaritalStatus href "../MaritalStatus/"
      PublicLife <|-- PoliticalAffiliation
        click PoliticalAffiliation href "../PoliticalAffiliation/"
      PublicLife <|-- PoliticalOpinion
        click PoliticalOpinion href "../PoliticalOpinion/"
      PublicLife <|-- Religion
        click Religion href "../Religion/"
      PublicLife <|-- SocialStatus
        click SocialStatus href "../SocialStatus/"
      

      
```





## Inheritance
* [Social](Social.md)
    * **PublicLife**
        * [Character](Character.md)
        * [CommunicationsMetadata](CommunicationsMetadata.md)
        * [GeneralReputation](GeneralReputation.md)
        * [Interaction](Interaction.md)
        * [MaritalStatus](MaritalStatus.md)
        * [SocialStatus](SocialStatus.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:PublicLife](https://w3id.org/lmodel/dpv/pd/PublicLife) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Public Life




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#PublicLife |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:PublicLife |
| native | pd:PublicLife |
| exact | dpv_pd:PublicLife, dpv_pd_owl:PublicLife |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PublicLife
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#PublicLife
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about public life
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Public Life
exact_mappings:
- dpv_pd:PublicLife
- dpv_pd_owl:PublicLife
is_a: Social
class_uri: pd:PublicLife

```
</details>

### Induced

<details>
```yaml
name: PublicLife
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#PublicLife
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about public life
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Public Life
exact_mappings:
- dpv_pd:PublicLife
- dpv_pd_owl:PublicLife
is_a: Social
class_uri: pd:PublicLife

```
</details></div>